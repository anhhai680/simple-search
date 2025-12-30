#!/usr/bin/env python3
"""
Generates React component with TypeScript and Redux integration.
Usage: python generate_react_component.py <component_name> [--with-redux] [--output-dir src/components]
Exit codes: 0=success, 1=invalid args, 2=file exists
"""
import sys
from pathlib import Path

def generate_component(name: str, with_redux: bool = False) -> str:
    """Generate React component."""
    component_name = name.capitalize()

    imports = """import React from 'react';
import { useState } from 'react';"""

    if with_redux:
        imports += """
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { /* import actions */ } from '../store/slices/{}Slice';""".format(name.lower())

    component = f"""
interface {component_name}Props {{
  // Add props here
}}

const {component_name}: React.FC<{component_name}Props> = (props) => {{
  const [state, setState] = useState<string>('');

  {f'''
  const dispatch = useDispatch();
  const {{ loading, error }} = useSelector((state: RootState) => state.{name.lower()});
  ''' if with_redux else ''}

  const handleSubmit = () => {{
    // Handle form submission
    console.log('Submitting:', state);
    {f'''
    // dispatch(submitAction(state));
    ''' if with_redux else ''}
  }};

  return (
    <div className="{name.lower()}-component">
      <h2>{component_name} Component</h2>
      <input
        type="text"
        value={{state}}
        onChange={{(e) => setState(e.target.value)}}
        placeholder="Enter {name.lower()}"
      />
      <button onClick={{handleSubmit}}>
        Submit
      </button>
      {f'''
      {{loading && <p>Loading...</p>}}
      {{error && <p>Error: {{error}}</p>}}
      ''' if with_redux else ''}
    </div>
  );
}};

export default {component_name};
"""

    return imports + component

def generate_redux_slice(name: str) -> str:
    """Generate Redux slice."""
    slice_name = name.lower()
    return f"""import {{ createSlice, createAsyncThunk }} from '@reduxjs/toolkit';

interface {name}State {{
  data: any[];
  loading: boolean;
  error: string | null;
}}

const initialState: {name}State = {{
  data: [],
  loading: false,
  error: null,
}};

// Async thunks
export const fetch{name} = createAsyncThunk(
  '{slice_name}/fetch',
  async () => {{
    // API call here
    const response = await fetch('/api/{slice_name}');
    return response.json();
  }}
);

const {slice_name}Slice = createSlice({{
  name: '{slice_name}',
  initialState,
  reducers: {{
    // Add synchronous reducers here
  }},
  extraReducers: (builder) => {{
    builder
      .addCase(fetch{name}.pending, (state) => {{
        state.loading = true;
        state.error = null;
      }})
      .addCase(fetch{name}.fulfilled, (state, action) => {{
        state.loading = false;
        state.data = action.payload;
      }})
      .addCase(fetch{name}.rejected, (state, action) => {{
        state.loading = false;
        state.error = action.error.message || 'Failed to fetch';
      }});
  }},
}});

export const {{ /* export actions */ }} = {slice_name}Slice.actions;
export default {slice_name}Slice.reducer;
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_react_component.py <component_name> [--with-redux] [--output-dir src/components]", file=sys.stderr)
        sys.exit(1)

    component_name = sys.argv[1]
    with_redux = "--with-redux" in sys.argv

    output_dir = "src/components"
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        if idx + 1 < len(sys.argv):
            output_dir = sys.argv[idx + 1]

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Generate component file
    component_file = output_path / f"{component_name}.tsx"
    if component_file.exists():
        print(f"Component file {component_file} already exists", file=sys.stderr)
        sys.exit(2)

    component_content = generate_component(component_name, with_redux)
    with open(component_file, 'w') as f:
        f.write(component_content)

    print(f"Generated React component: {component_file}")

    # Generate Redux slice if requested
    if with_redux:
        store_dir = Path("src/store/slices")
        store_dir.mkdir(parents=True, exist_ok=True)

        slice_file = store_dir / f"{component_name.lower()}Slice.ts"
        if slice_file.exists():
            print(f"Slice file {slice_file} already exists, skipping", file=sys.stderr)
        else:
            slice_content = generate_redux_slice(component_name)
            with open(slice_file, 'w') as f:
                f.write(slice_content)
            print(f"Generated Redux slice: {slice_file}")

    print("React component generation completed!")

if __name__ == "__main__":
    main()
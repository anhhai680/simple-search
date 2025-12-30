#!/bin/bash
# Setup Playwright for UI testing
# Usage: ./setup_playwright_tests.sh

set -e

echo "Setting up Playwright for UI testing..."

# Check if we're in a Node.js project
if [ ! -f "package.json" ]; then
    echo "Error: package.json not found. Run this in a Node.js project root." >&2
    exit 1
fi

# Install Playwright
npm install --save-dev @playwright/test

# Install browsers
npx playwright install

# Create test directory
mkdir -p tests/e2e

# Create playwright config
cat > playwright.config.ts << 'EOF'
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
});
EOF

# Create example test
cat > tests/e2e/example.spec.ts << 'EOF'
import { test, expect } from '@playwright/test';

test('homepage has title', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveTitle(/My App/);
});

test('navigation works', async ({ page }) => {
  await page.goto('/');

  await page.click('text=Users');
  await expect(page).toHaveURL(/.*users/);
});
EOF

# Add test script to package.json
if command -v jq &> /dev/null; then
    jq '.scripts.test = "playwright test" | .scripts["test:ui"] = "playwright test --ui"' package.json > package.json.tmp && mv package.json.tmp package.json
else
    echo "Please add these scripts to package.json manually:"
    echo '  "test": "playwright test",'
    echo '  "test:ui": "playwright test --ui"'
fi

echo "Playwright setup completed!"
echo "Next steps:"
echo "1. Update playwright.config.ts with your app's base URL"
echo "2. Write tests in tests/e2e/"
echo "3. Run 'npm run test' to execute tests"
echo "4. Run 'npm run test:ui' for visual test runner"
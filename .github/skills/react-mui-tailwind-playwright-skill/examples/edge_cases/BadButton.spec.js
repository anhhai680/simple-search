import { test, expect } from '@playwright/test';

test('BadButton has accessibility issues', async ({ page }) => {
  await page.goto('http://localhost:3000');

  const divButton = page.locator('div', { hasText: 'Click me' });
  await expect(divButton).toBeVisible();

  // This would ideally use axe-core to check violations
  // For demo, just check it's not a proper button
  const buttonTag = page.locator('button');
  await expect(buttonTag).not.toBeVisible();
});
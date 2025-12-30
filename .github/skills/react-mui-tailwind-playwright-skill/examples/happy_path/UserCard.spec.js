import { test, expect } from '@playwright/test';

test.describe('UserCard Component', () => {
  test('renders user information correctly', async ({ page }) => {
    // Assuming the component is rendered in a test app
    await page.goto('http://localhost:3000');

    const nameElement = page.locator('text=John Doe');
    const emailElement = page.locator('text=johndoe@example.com');
    const buttonElement = page.locator('button', { hasText: 'View Profile' });

    await expect(nameElement).toBeVisible();
    await expect(emailElement).toBeVisible();
    await expect(buttonElement).toBeVisible();
    await expect(buttonElement).toHaveClass(/bg-blue-500/);
  });

  test('button is clickable', async ({ page }) => {
    await page.goto('http://localhost:3000');

    const button = page.locator('button', { hasText: 'View Profile' });
    await button.click();
    // Add assertion for click action if applicable
  });
});
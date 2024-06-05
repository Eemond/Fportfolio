/**
 * @jest-environment jsdom
 */

const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.resolve(__dirname, '../index.html'), 'utf8');

describe('Menu functionality', () => {
    let document;

    beforeEach(() => {
        document = new jsdom.JSDOM(html, { runScripts: "dangerously" }).window.document;
        global.document = document;
        global.window = document.defaultView;

        require('../js/your-script.js'); // Replace with the actual path to your script
    });

    test('should show the menu when navToggle is clicked', () => {
        const navToggle = document.getElementById('nav-toggle');
        const navMenu = document.getElementById('nav-menu');

        navToggle.click();

        expect(navMenu.classList.contains('show-menu')).toBe(true);
    });

    test('should hide the menu when navClose is clicked', () => {
        const navToggle = document.getElementById('nav-toggle');
        const navMenu = document.getElementById('nav-menu');
        const navClose = document.getElementById('nav-close');

        navToggle.click();
        expect(navMenu.classList.contains('show-menu')).toBe(true);

        navClose.click();
        expect(navMenu.classList.contains('show-menu')).toBe(false);
    });

    test('should remove the menu when a nav__link is clicked', () => {
        const navToggle = document.getElementById('nav-toggle');
        const navMenu = document.getElementById('nav-menu');
        const navLink = document.querySelector('.nav__link');

        navToggle.click();
        expect(navMenu.classList.contains('show-menu')).toBe(true);

        navLink.click();
        expect(navMenu.classList.contains('show-menu')).toBe(false);
    });

    test('should add scroll-header class to header on scroll', () => {
        const header = document.getElementById('header');

        window.scrollY = 100;
        window.dispatchEvent(new Event('scroll'));

        expect(header.classList.contains('scroll-header')).toBe(true);
    });

    test('should add active-link class to the current section link on scroll', () => {
        const section = document.querySelector('section[id]');
        const link = document.querySelector(`.nav__menu a[href*="${section.id}"]`);

        window.scrollY = section.offsetTop;
        window.dispatchEvent(new Event('scroll'));

        expect(link.classList.contains('active-link')).toBe(true);
    });

    test('should show scroll-up button on scroll', () => {
        const scrollUp = document.getElementById('scroll-up');

        window.scrollY = 400;
        window.dispatchEvent(new Event('scroll'));

        expect(scrollUp.classList.contains('show-scroll')).toBe(true);
    });

    test('should toggle dark theme on button click', () => {
        const themeButton = document.getElementById('theme-button');
        const body = document.body;

        themeButton.click();
        expect(body.classList.contains('dark-theme')).toBe(true);

        themeButton.click();
        expect(body.classList.contains('dark-theme')).toBe(false);
    });
});

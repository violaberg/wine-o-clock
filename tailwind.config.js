/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        'parisienne': ['Parisienne', 'cursive'],
        'montserrat': ['Montserrat', 'sans-serif'],
      }
    },
    colors: {
      black: '#000000',
      gold: '#cc9933',
      maroon: '#4c0013',
      white: '#fafafa',
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}


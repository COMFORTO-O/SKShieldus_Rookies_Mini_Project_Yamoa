/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        'kbo': ['KBO-Dia-Gothic', 'Pretendard', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
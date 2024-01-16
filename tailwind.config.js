/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js,py}"],
  theme: {
    extend: {
      colors: {
        primary: "#0D5CA5", // Customize with your preferred color
        secondary: "#84BFF5",
        blue_300: "#C8E0F6",
        green_300: "#81BC78",
        yellow: "#EFEB8D",
        red: "#CA4747",
        green: "#66C057",
        black: "#282826",
        blue_100: "#F7FAFD",
        cart_blue: "#d4ebf2"

        // Add more custom colors as needed
      },
      fontFamily: {
        custom: ["roboto", "sans-serif"],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

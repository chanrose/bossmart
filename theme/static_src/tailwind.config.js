const colors = require("tailwindcss/colors");

module.exports = {
  mode: "jit",

  purge: [
    "../templates/**/*.html",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
    "../../../**/templates/**/*.html",
    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py' 
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    colors: {
      white: colors.white,
      gray: colors.gray,
      bgray: colors.blueGray,
      cgray: colors.coolGray,
      wgray: colors.warmGray,
      red: colors.red,
      blue: colors.sky,
      orange: colors.orange,
      yellow: colors.yellow,
      amber: colors.amber,
      lime: colors.lime,
      rose: colors.rose,
      fuchsia: colors.fuchsia,
      lime: colors.lime,
      green: colors.green,
      emerald: colors.emerald,
      teal: colors.teal,
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};

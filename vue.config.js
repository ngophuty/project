const { defineConfig } = require('@vue/cli-service')
const Path = require("path");

const OUTPUT_DIR = "./frontend/dist/";
const INPUT_DIR = "./frontend/src/";

module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: OUTPUT_DIR,
  pages: {
    index: {
      entry: `${INPUT_DIR}/main.js`,
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@": Path.resolve(__dirname, INPUT_DIR),
      },
      extensions: [".js", ".vue", ".json"],
    },
    devServer: {
      headers: { "Access-Control-Allow-Origin": "*" },
    },
  }
})

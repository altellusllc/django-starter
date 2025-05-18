const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

// Determine host/port for dev server public URL (defaults to localhost:8080)
const host = process.env.WEBPACK_DEV_HOST || 'localhost';
const port = process.env.WEBPACK_DEV_PORT || 8080;

module.exports = merge(common, {
  mode: 'development',
  devtool: 'eval-source-map',
  output: {
    filename: '[name].js',
    publicPath: `http://${host}:${port}/static/dist/`
  },
  devServer: {
    // bind to all network interfaces so external access is possible
    host: '0.0.0.0',
    // allow requests from any host
    allowedHosts: 'all',
    port: port,
    hot: true,
    headers: { 'Access-Control-Allow-Origin': '*' },
    devMiddleware: {
      publicPath: `http://${host}:${port}/static/dist/`,
      writeToDisk: true
    },
    static: {
      directory: './static/dist'
    }
  }
});
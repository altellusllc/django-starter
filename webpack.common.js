const path = require('path');

const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  context: __dirname,
  entry: {
    main: './assets/js/index.js'
  },
  output: {
    path: path.resolve(__dirname, 'static/dist/'),
    filename: '[name]-[contenthash].js',
    publicPath: '/static/dist/'
  },
  // Suppress Dart Sass legacy JS API deprecation warning
  ignoreWarnings: [
    /legacy JS API/i
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      },
      {
        test: /\.s?css$/,
        use: [
          process.env.NODE_ENV === 'production'
            ? MiniCssExtractPlugin.loader
            : 'style-loader',
          'css-loader',
          'postcss-loader',
          {
            loader: 'sass-loader',
            options: {
              implementation: require('sass'),
              sassOptions: {
                quietDeps: true
              }
            }
          }
        ]
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        type: 'asset',
        parser: {
          dataUrlCondition: {
            maxSize: 8 * 1024
          }
        }
      }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name]-[contenthash].css'
    }),
    new BundleTracker({ filename: './webpack-stats.json' })
  ],
  resolve: {
    extensions: ['.js', '.scss']
  }
};
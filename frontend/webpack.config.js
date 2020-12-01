const path = require('path');
const webpack = require('webpack');
module.exports = {
    entry: {
        main: path.resolve(__dirname, 'src/index.js'),
    },
    mode: 'development',
    output: {
        path: path.resolve(__dirname, '../backend/kanweek/static/kanweek/build/'),
        filename: '[name].js',
    },
    plugins: [
        // Do not output new files if there is an error
        new webpack.NoEmitOnErrorsPlugin(),
    ],
    resolve: {
        extensions: ['*', '.js', '.jsx'],
        modules: [
            path.resolve(__dirname, 'src'),
            path.resolve(__dirname, 'node_modules')
        ]
    },
    module: { 
        rules: [
            {
            test: /\.js$/,
            exclude: /node_modules/,
            use: ['babel-loader'],
            },
        ]
    },
}

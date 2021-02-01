module.exports = {
  transpileDependencies: [
    'vuetify'
  ]
}
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
    // on Windows you might want to set publicPath: "http://127.0.0.1:8080/" 
    publicPath: "http://192.168.2.148:8080/", 
    outputDir: './dist/',


    chainWebpack: config => {

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: './webpack-stats.json'}])

        config.output
            .filename('bundle.js')

        config.optimization
        	.splitChunks(false)

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            // the first 3 lines of the following code have been added to the configuration
            .public('http://192.168.2.148:8080')    
            .host('192.168.2.148')    
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .disableHostCheck(true)
            .headers({"Access-Control-Allow-Origin": ["\*"]})

    },
    

    // uncomment before executing 'npm run build' 
    // css: {
    //     extract: {
    //       filename: 'bundle.css',
    //       chunkFilename: 'bundle.css',
    //     },
    // }

    transpileDependencies: [
      'vuetify'
    ]

};
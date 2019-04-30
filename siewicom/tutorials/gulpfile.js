const {src,dest,task,series,watch,parallel} = require('gulp');

var rename = require('gulp-rename');
var browser = require('browser-sync').create();
var minifycss = require('gulp-minify-css');
var sass = require('gulp-sass');
var image = require('gulp-imagemin');

var reload = browser.reload;

var path ={
    'dir':'./',

    'client':'./templates/client/',
    'cms':'./templates/cms/',

    'src_css':'./static/src/css/',
    'src_image':'./static/src/img/',
    'src_js':'./static/src/js/',

    'dist_css':'./static/dist/css/',
    'dist_image':'./static/dist/img/',
    'dist_js':'./static/dist/js/'
};


//create server

function server(cf){
    browser.init({
        port:9000,
        server:{
            baseDir:path.dir,
            index:path.client+'article.html'
        }
    });
    cf();
}


function html(cf) {
    src(path.client+'*.html')
        .pipe(reload({stream:true}))
    cf();
}


function css(cf) {
    src(path.src_css+'*.scss')
        .pipe(sass())
        .pipe(minifycss())
        .pipe(rename({'suffix':'.min'}))
        .pipe(dest(path.dist_css))
        .pipe(reload({stream:true}))
    cf();
}

function images() {
    src(path.src_image+'*.*')
        .pipe(image())
        .pipe(dest(path.dist_image))
        .pipe(reload({stream:true}))
}

function watchs(cf) {
    watch(path.client+'*.html',series(html));
    watch(path.src_css+'*.scss',series(css));
    watch(path.src_image+'*.*',series(images));
    cf();
}


task('default',parallel(css,images,series(server,watchs)));
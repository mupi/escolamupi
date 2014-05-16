
(function (angular, markdown) {
    'use strict';

    angular.module('markdown.filters', ["ngSanitize"]).
        filter('markdown', ['$window', function($window) {
            return function(text) {
                //return text ? Markdown.getSanitizingConverter().makeHtml(text) : "";
                var tree = text ? markdown.toHTMLTree(markdown.parse(text)) : [];
                (function find_link_refs( htree ) {
                    if(Array.isArray(htree)){
                        if(htree[0] === "a"){
                            htree[1].target = "_blank";
                        } else {
                            htree.forEach(function(leaf){
                                if(Array.isArray(leaf)){
                                    find_link_refs(leaf);
                                }
                            });
                        }
                    }    
                })(tree)
            
                //find_link_refs(tree);                
                var html = markdown.toHTML(tree);
                return html;
            };
        }]);
})(angular, markdown);

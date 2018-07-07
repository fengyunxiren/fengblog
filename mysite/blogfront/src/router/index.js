import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import ArticleDetail from '@/components/ArticleDetail'
import CreateArticle from '@/components/CreateArticle'
import UpdateArticle from '@/components/UpdateArticle'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetail',
      component: ArticleDetail
    },
    {
      path: '/article/create',
      name: 'CreateArticle',
      component: CreateArticle
    },
    {
      path: '/article/update/:id',
      name: 'UpdateArticle',
      component: UpdateArticle
    }
  ]
})

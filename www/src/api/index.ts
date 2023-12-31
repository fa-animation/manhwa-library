import axios from 'axios'
import getConfig from 'next/config'

const { publicRuntimeConfig } = getConfig()

const api = axios.create({
  baseURL: publicRuntimeConfig.apiURL
})

export default api

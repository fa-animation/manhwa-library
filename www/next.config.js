/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  publicRuntimeConfig: {
    apiURL: process.env.API_URL
  },
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'media.kitsu.io'
      }
    ]
  }
}

module.exports = nextConfig

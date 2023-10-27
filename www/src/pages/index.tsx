import type { GetStaticProps } from 'next'
import Head from 'next/head'
import HeroPage from '@/containers/HeroPage'
import CardGrid from '@/components/card-grid'
import Explore from '@/components/explore'
import LastCard from '@/components/last-grids'
import api from '@/api/'

export interface MangaProps {
  id: string
  title: string
  slug: string
  description: string
  status_progress: string
  ratting: number
  image: string
  view_count: number
  year_published: string
  author: string
  artist: string
  type_book: string
}

export interface MangaT {
  data: MangaProps[]
}

export interface ArrayDataProps {
  lastHomeManga: MangaT
}

export const getStaticProps: GetStaticProps = async (context: any) => {
  const { data: lastHomeManga } = await api.get<MangaT>(
    '/v1/manga/?order_by=created_at&limit=5'
  )
  return {
    props: {
      lastHomeManga
    },
    revalidate: 60000
  }
}

export default function Home({ lastHomeManga }: ArrayDataProps) {
  return (
    <>
      <Head>
        <title>Manga Library</title>
      </Head>
      <HeroPage />
      <CardGrid />
      <LastCard lastHomeManga={lastHomeManga} />
      <Explore />
    </>
  )
}

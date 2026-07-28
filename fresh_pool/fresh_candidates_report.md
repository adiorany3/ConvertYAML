# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=258ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-97MS` (url=227ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=224ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS` (url=201ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-119MS` (url=231ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=210ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=227ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS` (url=261ms, nekobox=266ms, status=yes)
9. `AKUN-009-EU-VLESS-WS-129MS` (url=232ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS` (url=277ms, nekobox=266ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-150MS` (url=368ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=206ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-171MS` (url=287ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-186MS` (url=560ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-150MS` (url=238ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-183MS` (url=351ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-290MS` (url=556ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-294MS` (url=567ms, status=HTTP 204)
19. `AKUN-025-UNKNOWN-VLESS-WS-409MS` (url=663ms, status=HTTP 204)
20. `AKUN-026-SUKARIO-VLESS-WS-456MS` (url=731ms, status=HTTP 204)
21. `AKUN-030-UNKNOWN-VLESS-WS-515MS` (url=851ms, status=HTTP 204)
22. `AKUN-031-UNKNOWN-VLESS-WS-517MS` (url=862ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-531MS` (url=1304ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-546MS` (url=894ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-701MS` (url=1326ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

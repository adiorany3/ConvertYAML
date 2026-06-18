# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=283ms, nekobox=276ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=264ms, nekobox=189ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-115MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=267ms, nekobox=181ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-125MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-125MS` (url=271ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=315ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-189MS` (url=395ms, status=HTTP 204)
16. `AKUN-017-CONFLU-VLESS-WS-255MS` (url=567ms, status=HTTP 204)
17. `AKUN-019-WPENG-VLESS-WS-293MS` (url=641ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-284MS` (url=635ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-359MS` (url=919ms, status=HTTP 204)
20. `AKUN-024-ADF-VLESS-WS-88MS` (url=275ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

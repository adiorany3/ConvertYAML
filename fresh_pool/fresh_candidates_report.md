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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=275ms, nekobox=289ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=255ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=236ms, nekobox=258ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=259ms, nekobox=182ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=263ms, nekobox=191ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=269ms, nekobox=175ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=250ms, nekobox=189ms, status=no)
8. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=248ms, nekobox=186ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS` (url=286ms, nekobox=185ms, status=no)
11. `AKUN-005-UNKNOWN-VLESS-WS-93MS`
12. `AKUN-012-DEV-VLESS-WS-86MS` (url=287ms, nekobox=209ms, status=no)
13. `AKUN-006-UNKNOWN-VLESS-WS-96MS`
14. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS`
15. `AKUN-008-UNKNOWN-VLESS-WS-100MS`
16. `AKUN-009-UNKNOWN-VLESS-WS-113MS`
17. `AKUN-010-UNKNOWN-VLESS-WS-94MS`
18. `AKUN-018-UNKNOWN-VLESS-WS-138MS` (url=299ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-87MS` (url=260ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-255MS` (url=557ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-304MS` (url=612ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-309MS` (url=667ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-309MS` (url=665ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-295MS` (url=658ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-284MS` (url=527ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

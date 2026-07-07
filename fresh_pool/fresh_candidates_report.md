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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-100MS` (url=302ms, nekobox=314ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-110MS` (url=280ms, nekobox=305ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-108MS` (url=290ms, nekobox=301ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-103MS` (url=328ms, nekobox=315ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=305ms, nekobox=322ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-114MS` (url=299ms, nekobox=312ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=277ms, nekobox=340ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-128MS` (url=343ms, nekobox=324ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS` (url=281ms, nekobox=350ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS` (url=272ms, nekobox=278ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-117MS` (url=261ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-132MS` (url=305ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=285ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-148MS` (url=294ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-132MS` (url=305ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-137MS` (url=295ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-127MS` (url=289ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-118MS` (url=277ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-332MS` (url=792ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-339MS` (url=737ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-342MS` (url=702ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-331MS` (url=691ms, status=HTTP 204)
23. `AKUN-023-PUBLICDOMAINREGISTRY-NET-VLESS-WS-401MS` (url=758ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-358MS` (url=465ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-319MS` (url=697ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

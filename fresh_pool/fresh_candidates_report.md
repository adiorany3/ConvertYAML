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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-113MS` (url=282ms, nekobox=230ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-102MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-115MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-125MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-122MS`
6. `AKUN-005-ZVC-VLESS-WS-139MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-120MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-116MS`
9. `AKUN-008-DEV-VLESS-WS-142MS`
10. `AKUN-009-CCWU-VLESS-WS-126MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-110MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-124MS` (url=288ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-106MS` (url=298ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-116MS` (url=323ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-99MS` (url=306ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-193MS` (url=374ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-107MS` (url=248ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-185MS` (url=369ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-107MS` (url=280ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-93MS` (url=270ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-139MS` (url=304ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-128MS` (url=322ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-140MS` (url=324ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

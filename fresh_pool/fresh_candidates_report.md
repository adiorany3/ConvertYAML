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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=198ms, nekobox=236ms, status=yes)
2. `AKUN-002-090227-VLESS-WS-64MS` (url=200ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=206ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=205ms, nekobox=239ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-83MS` (url=206ms, nekobox=247ms, status=yes)
6. `AKUN-006-ZOOM-VLESS-WS-62MS` (url=219ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=195ms, nekobox=224ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-76MS` (url=213ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-63MS` (url=446ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=197ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-93MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=196ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-108MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-128MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-122MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-129MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-122MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-119MS` (url=207ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-90MS` (url=277ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-101MS` (url=217ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-119MS` (url=228ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-156MS` (url=237ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

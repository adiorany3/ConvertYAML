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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=247ms, nekobox=263ms, status=yes)
2. `AKUN-002-DIGITALOCEAN-VLESS-WS-100MS` (url=246ms, nekobox=289ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=262ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=258ms, nekobox=269ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=222ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=231ms, nekobox=264ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-100MS` (url=218ms, nekobox=278ms, status=yes)
8. `AKUN-008-WEBEX-VLESS-WS-94MS` (url=235ms, nekobox=245ms, status=yes)
9. `AKUN-009-WEBEX-VLESS-WS-102MS` (url=238ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS` (url=236ms, nekobox=232ms, status=yes)
11. `AKUN-011-MYBB-VLESS-WS-120MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-115MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-127MS` (url=428ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-124MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=255ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-122MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-117MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-103MS` (url=251ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-104MS` (url=873ms, status=HTTP 204)
21. `AKUN-021-ZVC-VLESS-WS-133MS` (url=243ms, status=HTTP 204)
22. `AKUN-022-COMPREND-NET-VLESS-WS-139MS` (url=240ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-120MS` (url=252ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-137MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-383MS` (url=798ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

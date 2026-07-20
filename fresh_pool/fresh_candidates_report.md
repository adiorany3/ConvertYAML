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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=219ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=201ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=228ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=231ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS` (url=231ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=229ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-113MS` (url=206ms, nekobox=244ms, status=yes)
8. `AKUN-008-DIXONS-VLESS-WS-92MS` (url=233ms, nekobox=265ms, status=yes)
9. `AKUN-009-SAVVY-7-VLESS-WS-104MS` (url=236ms, nekobox=262ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-84MS` (url=201ms, nekobox=237ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-112MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-UK-GB-DCL-01-20191003-VLESS-WS-127MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-166MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-123MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-147MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-146MS` (url=255ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-174MS` (url=243ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-120MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-192MS` (url=352ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-249MS` (url=517ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-258MS` (url=961ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-262MS` (url=2819ms, status=HTTP 204)
24. `AKUN-024-US-VLESS-WS-152MS` (url=204ms, status=HTTP 204)
25. `AKUN-025-466688-VLESS-WS-90MS` (url=233ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

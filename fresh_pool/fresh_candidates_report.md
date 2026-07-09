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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=231ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=243ms, nekobox=258ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-82MS` (url=237ms, nekobox=264ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-79MS` (url=276ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=232ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=255ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=234ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS` (url=227ms, nekobox=284ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=228ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS` (url=241ms, nekobox=206ms, status=no)
11. `AKUN-010-NODEHOST-VLESS-WS-91MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-96MS` (url=236ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-115MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-72MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-122MS` (url=244ms, status=HTTP 204)
16. `AKUN-016-ORG-VLESS-WS-77MS` (url=250ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=255ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-90MS` (url=284ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-107MS` (url=245ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-78MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-84MS` (url=251ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-108MS` (url=311ms, status=HTTP 204)
23. `AKUN-023-TENCENT-VLESS-WS-108MS` (url=241ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-105MS` (url=266ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-261MS` (url=611ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

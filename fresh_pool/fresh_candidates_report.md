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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=223ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=204ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=226ms, nekobox=256ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-73MS` (url=205ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=231ms, nekobox=241ms, status=yes)
6. `AKUN-006-MYBB-VLESS-WS-70MS` (url=206ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=244ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-75MS` (url=219ms, nekobox=227ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=208ms, nekobox=193ms, status=no)
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS`
12. `AKUN-012-ZVC-VLESS-WS-105MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-89MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-165MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-94MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-72MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-261MS` (url=553ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-251MS` (url=503ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-113MS` (url=305ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-258MS` (url=492ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-274MS` (url=585ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

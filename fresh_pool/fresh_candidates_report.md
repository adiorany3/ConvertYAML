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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=210ms, nekobox=240ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-66MS` (url=212ms, nekobox=261ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-78MS` (url=219ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=204ms, nekobox=276ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-80MS` (url=222ms, nekobox=269ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=220ms, nekobox=261ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-82MS` (url=227ms, nekobox=242ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-99MS` (url=218ms, nekobox=246ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-72MS` (url=227ms, nekobox=244ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-81MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-118MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-116MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-82MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-109MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-75MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-82MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-141MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-PAGES-VLESS-WS-118MS` (url=271ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-77MS` (url=230ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-232MS` (url=496ms, status=HTTP 204)
24. `AKUN-024-CELESTARA-VLESS-WS-256MS` (url=577ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-253MS` (url=543ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

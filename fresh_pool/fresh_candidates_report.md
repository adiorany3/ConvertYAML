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
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=210ms, nekobox=258ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-81MS` (url=232ms, nekobox=233ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-92MS` (url=201ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-93MS` (url=226ms, nekobox=7176ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-110MS` (url=289ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-121MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-118MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-DIXONS-VLESS-WS-125MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-135MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-129MS` (url=285ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-100MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-144MS` (url=284ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-137MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-95MS` (url=203ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-123MS` (url=250ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-251MS` (url=521ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

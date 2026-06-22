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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=225ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDWEBMANAGE-EU-FR-VLESS-WS-74MS` (url=224ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=213ms, nekobox=178ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=198ms, nekobox=200ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-88MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-128MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-124MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-109MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-96MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-246MS` (url=491ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-248MS` (url=576ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-241MS` (url=507ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-256MS` (url=555ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-265MS` (url=556ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-322MS` (url=495ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-258MS` (url=574ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

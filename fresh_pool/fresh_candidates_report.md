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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=201ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=207ms, nekobox=246ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-60MS` (url=209ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=202ms, nekobox=260ms, status=yes)
5. `AKUN-005-154-83-95-0-154-83-95-25-VLESS-WS-69MS` (url=222ms, nekobox=251ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=241ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=232ms, nekobox=240ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-81MS` (url=218ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=200ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=200ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-68MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-090227-VLESS-WS-77MS` (url=192ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-69MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-91MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-PUBLICDOMAINREGISTRY-NET-VLESS-WS-103MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-82MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-60MS` (url=204ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-121MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-125MS` (url=196ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-222MS` (url=499ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-234MS` (url=480ms, status=HTTP 204)
25. `AKUN-025-WPENG-VLESS-WS-269MS` (url=561ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

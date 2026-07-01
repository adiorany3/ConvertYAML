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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=208ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=202ms, nekobox=240ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=212ms, nekobox=232ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-84MS` (url=213ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=233ms, nekobox=237ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS` (url=201ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=215ms, nekobox=241ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=229ms, nekobox=228ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-111MS` (url=220ms, nekobox=245ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-144MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-ZOOM-VLESS-WS-79MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-106MS` (url=196ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-70MS` (url=208ms, status=HTTP 204)
15. `AKUN-016-DEV-VLESS-WS-102MS` (url=199ms, status=HTTP 204)
16. `AKUN-017-COMPREND-NET-VLESS-WS-84MS` (url=229ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-91MS` (url=207ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-250MS` (url=565ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-276MS` (url=559ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-250MS` (url=495ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-262MS` (url=481ms, status=HTTP 204)
22. `AKUN-025-MICROSOFT-VLESS-WS-311MS` (url=568ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-112MS` (url=208ms, status=HTTP 204)
24. `AKUN-027-DEV-VLESS-WS-71MS` (url=212ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-384MS` (url=675ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

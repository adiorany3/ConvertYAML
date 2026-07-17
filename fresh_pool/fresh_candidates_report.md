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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=208ms, nekobox=233ms, status=yes)
2. `AKUN-002-GO-DADDY-COM-LLC-VLESS-WS-58MS` (url=218ms, nekobox=248ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-67MS` (url=213ms, nekobox=243ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-66MS` (url=211ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, nekobox=250ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-64MS` (url=209ms, nekobox=237ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-75MS` (url=216ms, nekobox=250ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-77MS` (url=205ms, nekobox=235ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-74MS` (url=217ms, nekobox=244ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-79MS` (url=223ms, nekobox=249ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-81MS` (url=219ms, status=HTTP 204)
12. `AKUN-013-466688-VLESS-WS-69MS` (url=204ms, status=HTTP 204)
13. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-90MS` (url=232ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-66MS` (url=223ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-82MS` (url=230ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-64MS` (url=212ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-106MS` (url=199ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-82MS` (url=221ms, status=HTTP 204)
20. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-137MS` (url=241ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-145MS` (url=209ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-128MS` (url=211ms, status=HTTP 204)
23. `AKUN-024-DEV-VLESS-WS-67MS` (url=201ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-133MS` (url=215ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-84MS` (url=210ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

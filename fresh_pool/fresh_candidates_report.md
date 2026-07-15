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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=194ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=211ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=208ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=218ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=208ms, nekobox=231ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-83MS` (url=220ms, nekobox=240ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-62MS` (url=217ms, nekobox=259ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=205ms, nekobox=233ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=210ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=206ms, nekobox=235ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=205ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-GO-DADDY-COM-LLC-VLESS-WS-98MS` (url=241ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-106MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-CZ-LOTUNA-19970206-VLESS-WS-92MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-72MS` (url=201ms, status=HTTP 204)
18. `AKUN-018-PUBLICDOMAINREGISTRY-NET-VLESS-WS-126MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-109MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-90MS` (url=201ms, status=HTTP 204)
21. `AKUN-024-WEBEX-VLESS-WS-83MS` (url=228ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-242MS` (url=1663ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-260MS` (url=1463ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-256MS` (url=4380ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-244MS` (url=501ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

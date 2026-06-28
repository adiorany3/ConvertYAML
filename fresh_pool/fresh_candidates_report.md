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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=228ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=211ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=202ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDWEBMANAGE-EU-FR-VLESS-WS-71MS` (url=226ms, nekobox=249ms, status=yes)
5. `AKUN-005-DE-XTOM-20210903-VLESS-WS-78MS` (url=215ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=216ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=225ms, nekobox=233ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS` (url=206ms, nekobox=251ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=204ms, nekobox=234ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=210ms, nekobox=245ms, status=yes)
11. `AKUN-011-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-69MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-MEDIUM-VLESS-WS-73MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-91MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-122MS` (url=270ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-142MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-118MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-78MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-78MS` (url=200ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-68MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-240MS` (url=883ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-225MS` (url=493ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-245MS` (url=508ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-257MS` (url=547ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-251MS` (url=597ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-65MS` (url=352ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

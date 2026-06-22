# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=228ms, nekobox=228ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=220ms, nekobox=233ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS` (url=202ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=200ms, nekobox=233ms, status=yes)
5. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-85MS` (url=237ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=234ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=237ms, nekobox=7178ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-137MS`
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-87MS` (url=222ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=215ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-382MS` (url=774ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-369MS` (url=737ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-410MS` (url=3739ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-400MS` (url=849ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-407MS` (url=867ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-422MS` (url=1533ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-701MS` (url=972ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-440MS` (url=749ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-822MS` (url=1302ms, status=HTTP 204)
23. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-855MS` (url=1436ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-746MS` (url=1208ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

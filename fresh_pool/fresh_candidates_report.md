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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=218ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=253ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=217ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=225ms, nekobox=248ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-78MS` (url=226ms, nekobox=252ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-71MS` (url=223ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=210ms, nekobox=247ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-81MS` (url=284ms, nekobox=319ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=211ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=211ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-111MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-75MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-DE-CLOUDKLEYER-20190515-VLESS-WS-80MS` (url=511ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-94MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=336ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-127MS` (url=320ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-118MS` (url=251ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-176MS` (url=240ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-106MS` (url=230ms, status=HTTP 204)
22. `AKUN-024-LT-LRTC-20060503-VLESS-WS-221MS` (url=446ms, status=HTTP 204)
23. `AKUN-027-ROZANEH-VLESS-WS-332MS` (url=609ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-377MS` (url=736ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-403MS` (url=680ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

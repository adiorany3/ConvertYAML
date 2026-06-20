# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-ORACLE-VLESS-WS-66MS` (url=214ms, nekobox=262ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-68MS` (url=215ms, nekobox=245ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-58MS` (url=210ms, nekobox=252ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS` (url=252ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=217ms, nekobox=270ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=221ms, nekobox=226ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-67MS` (url=212ms, nekobox=251ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS` (url=200ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=207ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=220ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-112MS` (url=199ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-358MS` (url=758ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-402MS` (url=832ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-406MS` (url=872ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-422MS` (url=864ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-376MS` (url=896ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-361MS` (url=760ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-646MS` (url=898ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-672MS` (url=776ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-664MS` (url=952ms, status=HTTP 204)
22. `AKUN-028-UNKNOWN-VLESS-WS-631MS` (url=931ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-380MS` (url=3336ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

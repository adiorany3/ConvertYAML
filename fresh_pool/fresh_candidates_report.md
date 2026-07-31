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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=227ms, nekobox=234ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-69MS` (url=211ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=202ms, nekobox=230ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-57MS` (url=202ms, nekobox=225ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-61MS` (url=210ms, nekobox=252ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS` (url=216ms, nekobox=222ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-59MS` (url=199ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=200ms, nekobox=226ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-60MS` (url=198ms, nekobox=225ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-146MS` (url=333ms, nekobox=361ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-113MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-219MS` (url=479ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-240MS` (url=518ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-408MS` (url=721ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-387MS` (url=654ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-433MS` (url=822ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-436MS` (url=890ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-453MS` (url=773ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-431MS` (url=998ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-441MS` (url=760ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-433MS` (url=1175ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-441MS` (url=768ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-437MS` (url=740ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-461MS` (url=791ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-428MS` (url=797ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

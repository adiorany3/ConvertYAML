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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=205ms, nekobox=237ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-71MS` (url=217ms, nekobox=235ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-74MS` (url=198ms, nekobox=242ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-70MS` (url=202ms, nekobox=243ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-82MS` (url=200ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=216ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=205ms, nekobox=235ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-90MS` (url=268ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=207ms, nekobox=230ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=225ms, nekobox=242ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-83MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-92MS` (url=226ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-227MS` (url=491ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-234MS` (url=550ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-238MS` (url=525ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-242MS` (url=483ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-256MS` (url=544ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-247MS` (url=559ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-267MS` (url=564ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-394MS` (url=662ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-408MS` (url=696ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-424MS` (url=732ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-419MS` (url=641ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-447MS` (url=733ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-449MS` (url=775ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

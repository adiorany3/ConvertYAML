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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=236ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=233ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=219ms, nekobox=299ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS` (url=238ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=384ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=216ms, nekobox=230ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=221ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-58MS` (url=230ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=235ms, nekobox=232ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-77MS` (url=227ms, nekobox=259ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-81MS` (url=264ms, status=HTTP 204)
12. `AKUN-012-CLOUDWEBMANAGE-EU-FR-VLESS-WS-81MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-101MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-73MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-98MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-89MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-1PASSWORD-VLESS-WS-86MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-75MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-83MS` (url=273ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-101MS` (url=238ms, status=HTTP 204)
21. `AKUN-021-ADF-VLESS-WS-70MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-358MS` (url=796ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-370MS` (url=601ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-379MS` (url=824ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-407MS` (url=826ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

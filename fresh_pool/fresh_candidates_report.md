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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=213ms, nekobox=226ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-81MS` (url=208ms, nekobox=236ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-81MS` (url=214ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=207ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=240ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=197ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=222ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=223ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS` (url=221ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-81MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-102MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-69MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-70MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-79MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-135MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-76MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-98MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-111MS` (url=226ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-66MS` (url=224ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-114MS` (url=207ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-175MS` (url=369ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-226MS` (url=488ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-239MS` (url=484ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

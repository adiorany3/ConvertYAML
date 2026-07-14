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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=230ms, nekobox=229ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=230ms, nekobox=240ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=223ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=225ms, nekobox=239ms, status=yes)
6. `AKUN-006-DIXONS-VLESS-WS-95MS` (url=222ms, nekobox=263ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-104MS` (url=260ms, nekobox=259ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-104MS` (url=200ms, nekobox=237ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=217ms, nekobox=232ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-98MS` (url=202ms, nekobox=234ms, status=yes)
11. `AKUN-011-CZ-LOTUNA-19970206-VLESS-WS-88MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=260ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-91MS` (url=273ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-114MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-103MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-113MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-IDC-SG-VLESS-WS-124MS` (url=238ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-144MS` (url=273ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-254MS` (url=1195ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-266MS` (url=523ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-275MS` (url=597ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-431MS` (url=782ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-484MS` (url=884ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

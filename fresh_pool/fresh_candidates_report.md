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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=202ms, nekobox=249ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=218ms, nekobox=243ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=218ms, nekobox=246ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-80MS` (url=225ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=216ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=222ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, nekobox=249ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-84MS` (url=210ms, nekobox=178ms, status=no)
9. `AKUN-009-UNKNOWN-VLESS-WS-91MS` (url=200ms, nekobox=178ms, status=no)
10. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-81MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-62MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-77MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-95MS` (url=195ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-95MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-CZ-LOTUNA-19970206-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-104MS` (url=202ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-102MS` (url=223ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-83MS` (url=200ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-93MS` (url=216ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-120MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

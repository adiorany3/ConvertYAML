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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=231ms, nekobox=258ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=221ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=208ms, nekobox=186ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-74MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS` (url=227ms, nekobox=229ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-124MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-93MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-106MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-92MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-008500-VLESS-WS-73MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-96MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-MEDIUM-VLESS-WS-80MS` (url=195ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-358MS` (url=735ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-381MS` (url=819ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-400MS` (url=887ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-422MS` (url=2841ms, status=HTTP 204)
25. `AKUN-026-ADF-VLESS-WS-67MS` (url=204ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

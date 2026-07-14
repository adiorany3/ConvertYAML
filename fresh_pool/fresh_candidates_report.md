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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=210ms, nekobox=224ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=200ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=221ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=201ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, nekobox=226ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=208ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=219ms, nekobox=237ms, status=yes)
8. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-67MS` (url=216ms, nekobox=229ms, status=yes)
9. `AKUN-009-MYBB-VLESS-WS-79MS` (url=240ms, nekobox=246ms, status=yes)
10. `AKUN-010-ES-FORNEX-20160629-VLESS-WS-84MS` (url=206ms, nekobox=252ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-69MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-73MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-69MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-108MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-96MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-85MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-84MS` (url=242ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-79MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-79MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-POLICE-VLESS-WS-158MS` (url=234ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-116MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-94MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-VOV-VLESS-WS-167MS` (url=224ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

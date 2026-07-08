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
1. `AKUN-001-VULTR-VLESS-WS-73MS` (url=230ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=226ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=229ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS` (url=219ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=221ms, nekobox=262ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-104MS` (url=224ms, nekobox=251ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-80MS` (url=223ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=199ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=229ms, nekobox=234ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-90MS` (url=242ms, nekobox=230ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-83MS` (url=238ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-101MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-89MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-126MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-83MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-92MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-90MS` (url=204ms, status=HTTP 204)
18. `AKUN-018-WEBEX-VLESS-WS-90MS` (url=236ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-96MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-239MS` (url=531ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-252MS` (url=510ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-268MS` (url=568ms, status=HTTP 204)
23. `AKUN-023-CELESTARA-VLESS-WS-267MS` (url=567ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-243MS` (url=431ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-495MS` (url=842ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

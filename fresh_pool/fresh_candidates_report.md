# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-ZVC-VLESS-WS-89MS`
2. `AKUN-002-ZVC-VLESS-WS-71MS`
3. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=226ms, nekobox=192ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-127MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-145MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-149MS`
12. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=223ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-141MS` (url=225ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-153MS` (url=234ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-185MS` (url=238ms, status=HTTP 204)
16. `AKUN-018-RMGYVPN-VLESS-WS-154MS` (url=361ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-172MS` (url=274ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=3891ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-422MS` (url=772ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-293MS` (url=563ms, status=HTTP 204)
21. `AKUN-030-CLOUDFLARE-VLESS-WS-424MS` (url=712ms, status=HTTP 204)
22. `AKUN-031-DEV-VLESS-WS-129MS` (url=682ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-523MS` (url=861ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-590MS` (url=1543ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

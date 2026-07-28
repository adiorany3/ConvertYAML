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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=275ms, nekobox=338ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=281ms, nekobox=297ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=229ms, nekobox=274ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-96MS`
7. `AKUN-007-ZOOM-VLESS-WS-134MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-179MS`
10. `AKUN-010-090227-VLESS-WS-134MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-153MS` (url=336ms, status=HTTP 204)
12. `AKUN-013-SKK-VLESS-WS-221MS` (url=446ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-267MS` (url=588ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-130MS` (url=278ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-156MS` (url=309ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-224MS` (url=445ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-278MS` (url=3357ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-160MS` (url=374ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-447MS` (url=717ms, status=HTTP 204)
20. `AKUN-026-HOSTES-LLC-VLESS-WS-545MS` (url=891ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-477MS` (url=856ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-614MS` (url=919ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-675MS` (url=1519ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-612MS` (url=979ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-821MS` (url=1718ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

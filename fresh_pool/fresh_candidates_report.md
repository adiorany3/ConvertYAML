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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-130MS` (url=261ms, nekobox=227ms, status=no)
2. `AKUN-002-DEV-VLESS-WS-128MS` (url=233ms, nekobox=227ms, status=no)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-130MS` (url=237ms, nekobox=223ms, status=no)
4. `AKUN-001-UNKNOWN-VLESS-WS-133MS`
5. `AKUN-002-UNKNOWN-VLESS-WS-128MS`
6. `AKUN-006-DEV-VLESS-WS-132MS` (url=240ms, nekobox=230ms, status=no)
7. `AKUN-007-DEV-VLESS-WS-134MS` (url=237ms, nekobox=228ms, status=no)
8. `AKUN-008-DEV-VLESS-WS-131MS` (url=238ms, nekobox=225ms, status=no)
9. `AKUN-003-UNKNOWN-VLESS-WS-136MS`
10. `AKUN-004-CLOUDFLARE-VLESS-WS-134MS`
11. `AKUN-011-DEV-VLESS-WS-130MS` (url=231ms, nekobox=224ms, status=no)
12. `AKUN-012-UNKNOWN-VLESS-WS-131MS` (url=257ms, nekobox=230ms, status=no)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-139MS` (url=245ms, nekobox=229ms, status=no)
14. `AKUN-005-CLOUDFLARE-VLESS-WS-135MS`
15. `AKUN-006-CLOUDFLARE-VLESS-WS-135MS`
16. `AKUN-007-CLOUDFLARE-VLESS-WS-149MS`
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=250ms, nekobox=228ms, status=no)
18. `AKUN-008-BIGCOMMERCE-VLESS-WS-132MS`
19. `AKUN-019-DEV-VLESS-WS-130MS` (url=238ms, nekobox=229ms, status=no)
20. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
21. `AKUN-021-UNKNOWN-VLESS-WS-141MS` (url=239ms, nekobox=230ms, status=no)
22. `AKUN-010-CLOUDFLARE-VLESS-WS-191MS`
23. `AKUN-023-CLOUDFLARE-VLESS-WS-139MS` (url=321ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-390MS` (url=3502ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-395MS` (url=786ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

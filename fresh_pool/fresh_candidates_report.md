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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-125MS` (url=231ms, nekobox=226ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-130MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-128MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-131MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-124MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-132MS` (url=238ms, nekobox=231ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-137MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-141MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=233ms, nekobox=223ms, status=no)
10. `AKUN-007-UNKNOWN-VLESS-WS-142MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-135MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-142MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-207MS`
14. `AKUN-016-090227-VLESS-WS-228MS` (url=498ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-198MS` (url=342ms, status=HTTP 204)
16. `AKUN-018-NET-141-11-202-0-23-VLESS-WS-343MS` (url=690ms, status=HTTP 204)
17. `AKUN-021-UNKNOWN-VLESS-WS-129MS` (url=850ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-493MS` (url=892ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-131MS` (url=729ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-602MS` (url=921ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-597MS` (url=982ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-664MS` (url=3790ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-657MS` (url=1068ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-845MS` (url=1577ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-818MS` (url=957ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
